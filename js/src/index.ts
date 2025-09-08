export type Geometry = { type: 'Point'; coordinates: number[] };

export type AddressProperties = {
  ulb_lgd: string;
  street_name: string;
  house_number: string;
  locality: string;
  city: string;
  state: string;
  pin: string;
  primary_digipin: string;
  quality?: string;
};

export type AddressFeature = {
  type: 'Feature';
  properties: AddressProperties;
  geometry: Geometry;
};

export type ItemsParams = {
  limit?: number;
  offset?: number;
  bbox?: string;
  pin?: string;
  city?: string;
  ulb_lgd?: string;
  digipin?: string;
};

export async function listAddresses(
  baseUrl: string,
  limitOrParams: number | ItemsParams = 100
): Promise<AddressFeature[]> {
  const url = new URL('/collections/addresses/items', baseUrl);
  if (typeof limitOrParams === 'number') {
    url.searchParams.set('limit', String(limitOrParams));
  } else {
    const p = limitOrParams;
    if (p.limit != null) url.searchParams.set('limit', String(p.limit));
    if (p.offset != null) url.searchParams.set('offset', String(p.offset));
    if (p.bbox) url.searchParams.set('bbox', p.bbox);
    if (p.pin) url.searchParams.set('pin', p.pin);
    if (p.city) url.searchParams.set('city', p.city);
    if (p.ulb_lgd) url.searchParams.set('ulb_lgd', p.ulb_lgd);
    if (p.digipin) url.searchParams.set('digipin', p.digipin);
  }
  const resp = await fetch(url);
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  const data = await resp.json();
  return (data.features ?? []) as AddressFeature[];
}
