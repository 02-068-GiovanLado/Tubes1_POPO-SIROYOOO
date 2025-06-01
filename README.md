# Tubes STIGMA-RC-Kelompok POPO SIROYOOO–Bot Diamonds💎

## I. Penjelasan Singkat Algoritma Greedy yang Diimplementasikan

Program ini dirancang sebagai bot permainan Diamonds untuk berjalan secara otomatis dengan menjalankan keputusan cerdas pada setiap langkah berdasarkan kondisi terkini papan permainan. Kegunaan utama dari bot ini adalah implementasi algoritma greedy yang memandu setiap aksi bot, dimulai dari pengambilan diamond hingga kembali ke markas. Bot berinteraksi dengan game engine melalui sebuah script utama yang memproses logika bot dan menerjemahkannya menjadi aksi dalam permainan.

### Strategi Utama

1. **Prioritas Utama: Kembali ke Markas Jika Penuh**
   - Pada setiap giliran, bot pertama kali memeriksa:
     - Apakah lokasi markas (`base_position`) diketahui
     - Apakah jumlah diamond yang dibawa (`current_diamonds_held`) sudah mencapai atau melebihi kapasitas inventory (`inventory_size`)
   - Jika kedua kondisi terpenuhi, bot akan menetapkan posisi markas sebagai `target_pos`. Ini memastikan diamond yang sudah dikumpulkan bisa diamankan dan bot bisa mengambil diamond baru.

2. **Prioritas Kedua: Mencari dan Mengumpulkan Diamond (Jika Tidak Kembali ke Markas)**
   - Jika bot tidak perlu kembali ke markas, ia akan mencari diamond.
   - Bot mengidentifikasi semua `RedDiamondGameObject` dan `DiamondGameObject` yang ada di papan.
   - Bot kemudian mencari posisi diamond merah terdekat (`closest_red_pos`) dan diamond biru (`closest_blue_pos`) menggunakan fungsi `find_closest_diamond`.
   - Keputusan greedy berdasarkan jarak kompetitif:
     - Jika ada diamond merah ditemukan:
       - Bot menghitung jarak ke diamond merah tersebut.
       - Jika juga ada diamond biru ditemukan:
         - Bot menghitung jarak ke diamond biru tersebut.
         - Jika jarak ke diamond merah lebih kecil atau sama dengan jarak ke diamond biru, maka `target_pos` adalah `closest_red_pos`.
         - Jika tidak, `target_pos` adalah `closest_blue_pos`.
       - Jika tidak ada diamond biru (hanya merah yang ada), maka `target_pos` adalah `closest_red_pos`.
     - Jika tidak ada diamond merah tetapi ada diamond biru, maka `target_pos` adalah `closest_blue_pos`.

---

## II. Requirements dan Instalasi

### 1. Cara Menjalankan Game Engine

#### a. Requirement yang Harus Di-install
- Node.js: [https://nodejs.org/en](https://nodejs.org/en)  
- Docker Desktop: [https://www.docker.com/products/docker-desktop/)  
- Yarn:
  ```bash
  npm install --global yarn
  ```

#### b. Instalasi dan Konfigurasi Awal
1. Download source code (.zip) dari release game engine.
2. Extract zip tersebut, lalu masuk ke folder hasil extract dan buka terminal.
3. Masuk ke root directory dari project:
   ```bash
   cd tubes1-IF2110-game-engine-1.1.0
   ```
4. Install dependencies menggunakan Yarn:
   ```bash
   yarn
   ```
5. Setup default environment variable:
   - **Windows**:
     ```bash
     ./scripts/copy-env.bat
     ```
   - **Linux/macOS**:
     ```bash
     chmod +x ./scripts/copy-env.sh
     ./scripts/copy-env.sh
     ```
6. Setup local database (pastikan Docker Desktop sudah dibuka):
   ```bash
   docker compose up -d database
   ```
   Lalu jalankan:
   - **Windows**:
     ```bash
     ./scripts/setup-db-prisma.bat
     ```
   - **Linux/macOS**:
     ```bash
     chmod +x ./scripts/setup-db-prisma.sh
     ./scripts/setup-db-prisma.sh
     ```

#### c. Build
```bash
npm run build
```

#### d. Run
```bash
npm run start
```

---

### 2. Cara Menjalankan Bot

#### a. Requirement yang Harus Di-install
- Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

#### b. Instalasi dan Konfigurasi Awal
1. Download source code (.zip) dari release bot starter pack.
2. Extract zip tersebut, lalu masuk ke folder hasil extract dan buka terminal.
3. Masuk ke root directory dari project:
   ```bash
   cd tubes1-IF2110-bot-starter-pack-1.0.1
   ```
4. Install dependencies menggunakan pip:
   ```bash
   pip install -r requirements.txt
   ```

#### c. Run

- Menjalankan satu bot:
  ```bash
  python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo
  ```

- Menjalankan beberapa bot sekaligus:
  - **Windows**:
    ```bash
    ./run-bots.bat
    ```
  - **Linux/macOS**:
    ```bash
    ./run-bots.sh
    ```

---

## IV. Author

Kelompok 10 (POPO SIROYOOO)

| Nama                      | NIM       | 
| --------------------------| --------- |
| Giovan Lado               | 123140068 | 
| Nadine Aura Rahmadhani    | 123140195 | 
| Tengku Hafid Diraputra    | 123140043 |
