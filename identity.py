import uuid
import hashlib
import json

NAMESPACE_UUID = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')  # DNS namespace, can be replaced

def canonical_serialize(entity_state: dict) -> str:
    """
    Canonically serialize an entity's state to a JSON string with sorted keys.
    """
    return json.dumps(entity_state, sort_keys=True, separators=(",", ":"))


def deterministic_uuid_v5(entity_state: dict) -> str:
    """
    Generate a deterministic UUIDv5 from the SHA-256 hash of the entity's canonical serialized state.
    """
    serialized = canonical_serialize(entity_state)
    sha256_hash = hashlib.sha256(serialized.encode('utf-8')).hexdigest()
    # Use the first 32 characters of the SHA-256 hash as the 'name' for UUIDv5
    uuid_v5 = uuid.uuid5(NAMESPACE_UUID, sha256_hash[:32])
    return str(uuid_v5)

# Example usage:
if __name__ == "__main__":
    example_entity = {"type": "function", "code": "def f(x): return x+1", "version": 1}
    print("UUIDv5:", deterministic_uuid_v5(example_entity))
