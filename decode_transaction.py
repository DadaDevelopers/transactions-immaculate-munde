from bitcoin.core import lx, b2lx, CTransaction
from bitcoin.core import x
from bitcoin import SelectParams

def decode_tx(hex_string):
    """Decode and print Bitcoin transaction details."""
    SelectParams('mainnet')  # or 'regtest'/'testnet' depending on context

    tx_bytes = bytes.fromhex(hex_string)
    tx = CTransaction.deserialize(tx_bytes)

    print("\n=== Transaction Details ===")
    print(f"Version: {tx.nVersion}")
    print(f"Number of Inputs: {len(tx.vin)}")
    print(f"Number of Outputs: {len(tx.vout)}")
    print(f"Locktime: {tx.nLockTime}")
    print("\nInputs:")
    for vin in tx.vin:
        print(f"  TXID: {b2lx(vin.prevout.hash)}")
        print(f"  Vout: {vin.prevout.n}")
        print(f"  ScriptSig: {vin.scriptSig.hex()}")
        print(f"  Sequence: {vin.nSequence}")
    print("\nOutputs:")
    for i, vout in enumerate(tx.vout):
        print(f"  Output {i+1}:")
        print(f"    Value: {vout.nValue / 1e8} BTC")
        print(f"    ScriptPubKey: {vout.scriptPubKey.hex()}")

# Test using given hex
if __name__ == "__main__":
    tx_hex = "0200000000010131811cd355c357e0e01437d9bcf690df824e9ff785012b6115dfae3d8e8b36c10100000000fdffffff0220a107000000000016001485d78eb795bd9c8a21afefc8b6fdaedf718368094c08100000000000160014840ab165c9c2555d4a31b9208ad806f89d2535e20247304402207bce86d430b58bb6b79e8c1bbecdf67a530eff3bc61581a1399e0b28a741c0ee0220303d5ce926c60bf15577f2e407f28a2ef8fe8453abd4048b716e97dbb1e3a85c01210260828bc77486a55e3bc6032ccbeda915d9494eda17b4a54dbe3b24506d40e4ff43030e00"
    decode_tx(tx_hex)
