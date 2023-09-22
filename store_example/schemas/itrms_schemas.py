def item_serializer(item) -> dict:
        return {
            "id": item["_id"],
            'name': item['name'],
            'description': item['description'],
            'catagory': item['catagory'],
            'mrp': int(item['mrp']),
            'selling_price': int(item['selling_price'])
        }

def items_serializer(items) -> list:
    return [item_serializer(item) for item in items]