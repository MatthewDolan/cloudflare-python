# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .prefixes import (
    Prefixes,
    AsyncPrefixes,
    PrefixesWithRawResponse,
    AsyncPrefixesWithRawResponse,
    PrefixesWithStreamingResponse,
    AsyncPrefixesWithStreamingResponse,
)
from .services import (
    Services,
    AsyncServices,
    ServicesWithRawResponse,
    AsyncServicesWithRawResponse,
    ServicesWithStreamingResponse,
    AsyncServicesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .address_maps import (
    AddressMaps,
    AsyncAddressMaps,
    AddressMapsWithRawResponse,
    AsyncAddressMapsWithRawResponse,
    AddressMapsWithStreamingResponse,
    AsyncAddressMapsWithStreamingResponse,
)
from .loa_documents import (
    LOADocuments,
    AsyncLOADocuments,
    LOADocumentsWithRawResponse,
    AsyncLOADocumentsWithRawResponse,
    LOADocumentsWithStreamingResponse,
    AsyncLOADocumentsWithStreamingResponse,
)
from .prefixes.prefixes import Prefixes, AsyncPrefixes
from .address_maps.address_maps import AddressMaps, AsyncAddressMaps
from .loa_documents.loa_documents import LOADocuments, AsyncLOADocuments

__all__ = ["Addresses", "AsyncAddresses"]


class Addresses(SyncAPIResource):
    @cached_property
    def services(self) -> Services:
        return Services(self._client)

    @cached_property
    def address_maps(self) -> AddressMaps:
        return AddressMaps(self._client)

    @cached_property
    def loa_documents(self) -> LOADocuments:
        return LOADocuments(self._client)

    @cached_property
    def prefixes(self) -> Prefixes:
        return Prefixes(self._client)

    @cached_property
    def with_raw_response(self) -> AddressesWithRawResponse:
        return AddressesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesWithStreamingResponse:
        return AddressesWithStreamingResponse(self)


class AsyncAddresses(AsyncAPIResource):
    @cached_property
    def services(self) -> AsyncServices:
        return AsyncServices(self._client)

    @cached_property
    def address_maps(self) -> AsyncAddressMaps:
        return AsyncAddressMaps(self._client)

    @cached_property
    def loa_documents(self) -> AsyncLOADocuments:
        return AsyncLOADocuments(self._client)

    @cached_property
    def prefixes(self) -> AsyncPrefixes:
        return AsyncPrefixes(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddressesWithRawResponse:
        return AsyncAddressesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesWithStreamingResponse:
        return AsyncAddressesWithStreamingResponse(self)


class AddressesWithRawResponse:
    def __init__(self, addresses: Addresses) -> None:
        self._addresses = addresses

    @cached_property
    def services(self) -> ServicesWithRawResponse:
        return ServicesWithRawResponse(self._addresses.services)

    @cached_property
    def address_maps(self) -> AddressMapsWithRawResponse:
        return AddressMapsWithRawResponse(self._addresses.address_maps)

    @cached_property
    def loa_documents(self) -> LOADocumentsWithRawResponse:
        return LOADocumentsWithRawResponse(self._addresses.loa_documents)

    @cached_property
    def prefixes(self) -> PrefixesWithRawResponse:
        return PrefixesWithRawResponse(self._addresses.prefixes)


class AsyncAddressesWithRawResponse:
    def __init__(self, addresses: AsyncAddresses) -> None:
        self._addresses = addresses

    @cached_property
    def services(self) -> AsyncServicesWithRawResponse:
        return AsyncServicesWithRawResponse(self._addresses.services)

    @cached_property
    def address_maps(self) -> AsyncAddressMapsWithRawResponse:
        return AsyncAddressMapsWithRawResponse(self._addresses.address_maps)

    @cached_property
    def loa_documents(self) -> AsyncLOADocumentsWithRawResponse:
        return AsyncLOADocumentsWithRawResponse(self._addresses.loa_documents)

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithRawResponse:
        return AsyncPrefixesWithRawResponse(self._addresses.prefixes)


class AddressesWithStreamingResponse:
    def __init__(self, addresses: Addresses) -> None:
        self._addresses = addresses

    @cached_property
    def services(self) -> ServicesWithStreamingResponse:
        return ServicesWithStreamingResponse(self._addresses.services)

    @cached_property
    def address_maps(self) -> AddressMapsWithStreamingResponse:
        return AddressMapsWithStreamingResponse(self._addresses.address_maps)

    @cached_property
    def loa_documents(self) -> LOADocumentsWithStreamingResponse:
        return LOADocumentsWithStreamingResponse(self._addresses.loa_documents)

    @cached_property
    def prefixes(self) -> PrefixesWithStreamingResponse:
        return PrefixesWithStreamingResponse(self._addresses.prefixes)


class AsyncAddressesWithStreamingResponse:
    def __init__(self, addresses: AsyncAddresses) -> None:
        self._addresses = addresses

    @cached_property
    def services(self) -> AsyncServicesWithStreamingResponse:
        return AsyncServicesWithStreamingResponse(self._addresses.services)

    @cached_property
    def address_maps(self) -> AsyncAddressMapsWithStreamingResponse:
        return AsyncAddressMapsWithStreamingResponse(self._addresses.address_maps)

    @cached_property
    def loa_documents(self) -> AsyncLOADocumentsWithStreamingResponse:
        return AsyncLOADocumentsWithStreamingResponse(self._addresses.loa_documents)

    @cached_property
    def prefixes(self) -> AsyncPrefixesWithStreamingResponse:
        return AsyncPrefixesWithStreamingResponse(self._addresses.prefixes)
