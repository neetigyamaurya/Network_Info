import socket

import dns_lookup


def test_input_validation_accepts_valid_ipv4():
    assert dns_lookup.inputValidation("192.168.1.1") is True


def test_input_validation_rejects_invalid_ipv4():
    assert dns_lookup.inputValidation("999.168.1.1") is False
    assert dns_lookup.inputValidation("192.168.1") is False


def test_private_ip_detection():
    assert dns_lookup.is_private_ip("10.0.0.1") is True
    assert dns_lookup.is_private_ip("172.16.0.1") is True
    assert dns_lookup.is_private_ip("192.168.1.1") is True
    assert dns_lookup.is_private_ip("8.8.8.8") is False


def test_domain_validation_returns_ip(monkeypatch):
    monkeypatch.setattr(socket, "gethostbyname", lambda domain: "1.2.3.4")

    assert dns_lookup.domain_validation("example.com") == "1.2.3.4"


def test_domain_validation_handles_invalid_domain(monkeypatch):
    def raise_gaierror(domain):
        raise socket.gaierror

    monkeypatch.setattr(socket, "gethostbyname", raise_gaierror)

    assert dns_lookup.domain_validation("invalid.example") == "Invalid domain name"


def test_get_domain_by_ip_returns_hostname(monkeypatch):
    monkeypatch.setattr(socket, "gethostbyaddr", lambda ip: ("dns.example", [], [ip]))

    assert dns_lookup.get_domain_by_ip("1.2.3.4") == "dns.example"


def test_get_domain_by_ip_handles_missing_hostname(monkeypatch):
    def raise_herror(ip):
        raise socket.herror

    monkeypatch.setattr(socket, "gethostbyaddr", raise_herror)

    assert dns_lookup.get_domain_by_ip("1.2.3.4") == "Hostname not found"


def test_cross_validation_prints_lookup_chain(monkeypatch, capsys):
    monkeypatch.setattr(dns_lookup, "domain_validation", lambda domain: "1.2.3.4")
    monkeypatch.setattr(dns_lookup, "get_domain_by_ip", lambda ip: "dns.example")

    dns_lookup.cross_validation("example.com")

    assert capsys.readouterr().out == "example.com -> 1.2.3.4 -> dns.example\n"


def test_cross_validation_stops_on_invalid_domain(monkeypatch, capsys):
    monkeypatch.setattr(dns_lookup, "domain_validation", lambda domain: "Invalid domain name")

    dns_lookup.cross_validation("invalid.example")

    assert capsys.readouterr().out == "Invalid domain name\n"
