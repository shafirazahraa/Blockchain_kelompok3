from blockchain import Blockchain
import pow 
from pos import proof_of_stake
blockchain = Blockchain()

# ================================================
# TEMA: Perjalanan 1 tiket konser dari terbit -> dipakai
# Aktor 1 & 2 (asli dari modul) + Aktor 3 & 4 (tambahan sesuai tugas)
# Kategori tiket: Reguler, VIP, VVIP, Premium (isi salah satu di "kategori")
# ================================================

# 1. Promotor menerbitkan tiket
blockchain.add_block({
    "tiket_id": "TKT-001",
    "event": "Konser Musik Jakarta",
    "kategori": "VIP",
    "aktor": "Promotor",
    "aksi": "Menerbitkan tiket",
    "lokasi": "Jakarta"
})

# 2. Vendor Resmi menjual tiket ke publik
blockchain.add_block({
    "tiket_id": "TKT-001",
    "event": "Konser Musik Jakarta",
    "kategori": "VIP",
    "aktor": "Vendor Resmi",
    "aksi": "Menjual tiket ke pembeli",
    "lokasi": "Jakarta"
})

# 3. Reseller menjual ulang tiket (aktor tambahan #1)
blockchain.add_block({
    "tiket_id": "TKT-001",
    "event": "Konser Musik Jakarta",
    "kategori": "VIP",
    "aktor": "Reseller",
    "aksi": "Menjual ulang tiket",
    "lokasi": "Jakarta"
})

# 4. Penonton check-in di lokasi konser (aktor tambahan #2)
blockchain.add_block({
    "tiket_id": "TKT-001",
    "event": "Konser Musik Jakarta",
    "kategori": "VIP",
    "aktor": "Penonton",
    "aksi": "Check-in di pintu masuk",
    "lokasi": "Jakarta"
})

for block in blockchain.chain:

    print("=" * 50)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())


# ================================================
# EKSPERIMEN PROOF OF WORK
# Menambang ulang salah satu block (misal block terakhir) 
# untuk memenuhi target difficulty
# ================================================

print("\n" + "=" * 50)
print("PROOF OF WORK")

difficulty = 4
target_block = blockchain.chain[-1]  # block check-in penonton

print("\nData Block      :", target_block.data)
print("Difficulty       :", difficulty)

pow.proof_of_work(target_block, difficulty)

print("Nonce            :", target_block.nonce)
print("Hash             :", target_block.hash)


# ================================================
# EKSPERIMEN PROOF OF STAKE
# Simulasi pemilihan validator dari para aktor tiket
# ================================================

print("\n" + "=" * 50)
print("PROOF OF STAKE")

validators = {
    "Promotor": 10,
    "Vendor Resmi": 20,
    "Reseller": 30,
    "Penonton": 40
}

print("\nValidator:")
for validator, stake in validators.items():
    print(f"- {validator}: {stake} stake")

selected = proof_of_stake(validators)

print("\nValidator terpilih:", selected)