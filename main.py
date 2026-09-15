from blockchain import Blockchain

blockchain = Blockchain()


# 1. Promotor menerbitkan (mint) tiket sebagai aset digital
blockchain.add_block({
    "ticket_id": "TIX-2026-001",
    "event": "Cirebon Music Fest 2026",
    "category": "VIP",
    "actor": "Promotor",
    "action": "Mint Tiket (Issue)",
    "location": "Cirebon"
})

# 2. Pembeli pertama membeli tiket langsung dari promotor
blockchain.add_block({
    "ticket_id": "TIX-2026-001",
    "event": "Cirebon Music Fest 2026",
    "category": "VIP",
    "actor": "Pembeli Pertama",
    "action": "Beli Tiket (Primary Sale)",
    "location": "Cirebon"
})

# 3. Tiket dijual kembali melalui platform resale resmi
blockchain.add_block({
    "ticket_id": "TIX-2026-001",
    "event": "Cirebon Music Fest 2026",
    "category": "VIP",
    "actor": "Platform Resale",
    "action": "Transfer Kepemilikan (Resale)",
    "location": "Online"
})

# 4. Petugas venue memverifikasi tiket saat check-in di pintu masuk
blockchain.add_block({
    "ticket_id": "TIX-2026-001",
    "event": "Cirebon Music Fest 2026",
    "category": "VIP",
    "actor": "Petugas Venue",
    "action": "Verifikasi & Check-in",
    "location": "Gerbang Venue"
})


for block in blockchain.chain:

    print("=" * 50)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())