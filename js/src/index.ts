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

export async function listAddresses(baseUrl: string, limit = 100): Promise<AddressFeature[]> {
  const url = new URL('/collections/addresses/items', baseUrl);
  url.searchParams.set('limit', String(limit));
  const resp = await fetch(url);
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  const data = await resp.json();
  return (data.features ?? []) as AddressFeature[];
}
