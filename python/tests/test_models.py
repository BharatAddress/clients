from bharataddress_client.models import AddressFeature, AddressProperties, Geometry


def test_model_roundtrip():
    feat = AddressFeature(
        properties=AddressProperties(
            ulb_lgd="294690",
            street_name="Test",
            house_number="1",
            locality="Loc",
            city="City",
            state="State",
            pin="560001",
            primary_digipin="AAA-BBB-1111",
        ),
        geometry=Geometry(coordinates=[77.0, 12.0]),
    )
    d = feat.model_dump()
    assert d["type"] == "Feature"
