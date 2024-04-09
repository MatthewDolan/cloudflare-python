# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .records import (
    Records,
    AsyncRecords,
    RecordsWithRawResponse,
    AsyncRecordsWithRawResponse,
    RecordsWithStreamingResponse,
    AsyncRecordsWithStreamingResponse,
)
from .firewall import (
    FirewallResource,
    AsyncFirewallResource,
    FirewallResourceWithRawResponse,
    AsyncFirewallResourceWithRawResponse,
    FirewallResourceWithStreamingResponse,
    AsyncFirewallResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .analytics import (
    Analytics,
    AsyncAnalytics,
    AnalyticsWithRawResponse,
    AsyncAnalyticsWithRawResponse,
    AnalyticsWithStreamingResponse,
    AsyncAnalyticsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .firewall.firewall import FirewallResource, AsyncFirewallResource
from .analytics.analytics import Analytics, AsyncAnalytics

__all__ = ["DNS", "AsyncDNS"]


class DNS(SyncAPIResource):
    @cached_property
    def records(self) -> Records:
        return Records(self._client)

    @cached_property
    def analytics(self) -> Analytics:
        return Analytics(self._client)

    @cached_property
    def firewall(self) -> FirewallResource:
        return FirewallResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self)


class AsyncDNS(AsyncAPIResource):
    @cached_property
    def records(self) -> AsyncRecords:
        return AsyncRecords(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalytics:
        return AsyncAnalytics(self._client)

    @cached_property
    def firewall(self) -> AsyncFirewallResource:
        return AsyncFirewallResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self)


class DNSWithRawResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

    @cached_property
    def records(self) -> RecordsWithRawResponse:
        return RecordsWithRawResponse(self._dns.records)

    @cached_property
    def analytics(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self._dns.analytics)

    @cached_property
    def firewall(self) -> FirewallResourceWithRawResponse:
        return FirewallResourceWithRawResponse(self._dns.firewall)


class AsyncDNSWithRawResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

    @cached_property
    def records(self) -> AsyncRecordsWithRawResponse:
        return AsyncRecordsWithRawResponse(self._dns.records)

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self._dns.analytics)

    @cached_property
    def firewall(self) -> AsyncFirewallResourceWithRawResponse:
        return AsyncFirewallResourceWithRawResponse(self._dns.firewall)


class DNSWithStreamingResponse:
    def __init__(self, dns: DNS) -> None:
        self._dns = dns

    @cached_property
    def records(self) -> RecordsWithStreamingResponse:
        return RecordsWithStreamingResponse(self._dns.records)

    @cached_property
    def analytics(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self._dns.analytics)

    @cached_property
    def firewall(self) -> FirewallResourceWithStreamingResponse:
        return FirewallResourceWithStreamingResponse(self._dns.firewall)


class AsyncDNSWithStreamingResponse:
    def __init__(self, dns: AsyncDNS) -> None:
        self._dns = dns

    @cached_property
    def records(self) -> AsyncRecordsWithStreamingResponse:
        return AsyncRecordsWithStreamingResponse(self._dns.records)

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self._dns.analytics)

    @cached_property
    def firewall(self) -> AsyncFirewallResourceWithStreamingResponse:
        return AsyncFirewallResourceWithStreamingResponse(self._dns.firewall)
