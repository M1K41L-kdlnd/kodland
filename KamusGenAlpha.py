meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SKIBIDI": "Kata untuk mengatakan sesuatu yang tidak bagus",
            "KAICENAT": "Seorang Streamer Asal Amerika",
            "SIGMA": "Seorang yang sangat independen"
            "LOOKSMAXXING": "Kata untuk orang yang sedang mewing"
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # Apa yang harus kita lakukan jika kata itu ditemukan?
else: print ('maaf kata yang anda cari tidak ada')
