# Kompass Provider Specification

Status:
Production Candidate

Provider Type:
Commercial Directory

Protocol:
HTTPS

Authentication:
None (Public Search)

Response Format:
HTML

Search Query:
Verified

Pagination:
Supported

Provider Confidence:
High

--------------------------------------------------

Search Behaviour

The provider performs semantic search.

The returned companies are not guaranteed to belong
to the requested country.

Country filtering must therefore be performed by Atlas.

--------------------------------------------------

Company Record

Each company record contains:

- Company Name
- Company URL
- Location
- Description
- Product Categories

Optional:

- Website
- Phone
- Email

--------------------------------------------------

Primary Selectors

Container:
div.prod_list

Company Name:
span.titleSpan

Location:
span.placeText

Description:
p.description

Supplier Categories:
ul > li

--------------------------------------------------

Known Limitations

Search is semantic rather than geographical.

Not every listing exposes direct contact details.

HTML structure should be considered versioned and
validated against production fixtures.

--------------------------------------------------

Definition of Done

KompassProvider shall convert one HTML fixture into
BuyerRecord objects without manual intervention.

