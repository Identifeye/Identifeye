def convertData(request):
    return [
        request.account_name_hash,
        request.character_name_hash,
        request.ip_hash,
        request.uuid_hash,
        request.ip_location_hash,
        request.is_banned,
        request.active_playtime
        ]