SELECT * FROM user_words;
CREATE TABLE user_grammers (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    grammer_id INT REFERENCES grammers(grammer_id) ON DELETE CASCADE,
    dutch_sentence TEXT,
    turkish_sentence TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE quiz_results (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    quiz_type VARCHAR(20) CHECK (quiz_type IN ('test', 'writing', 'speaking')) NOT NULL,
    score INT CHECK (score BETWEEN 0 AND 100),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE hints (
    hint_id SERIAL PRIMARY KEY,
    word_id INT REFERENCES words(word_id) ON DELETE CASCADE,
    hint_text TEXT NOT NULL
);
INSERT INTO users (username, email, password, role) 
VALUES 
    ('yasin', 'yasin@mail.com', 'hashed_password_1', 'admin'),
    ('ahmet', 'ahmet@mail.com', 'hashed_password_2', 'user');
SELECT * 
FROM users;

INSERT INTO words (word_name, word_type, meaning, description) 
VALUES 
    ('brengen', 'fiil', 'getirmek', 'Bu fiil bir şeyi bir yerden bir yere taşımak anlamına gelir.'),
    ('huis', 'isim', 'ev', 'Yaşanılan yapı, konut.');
SELECT * 
FROM words;

SELECT * 
FROM word_variations;

ALTER TABLE word_variations 
ADD COLUMN meaning VARCHAR(100) NOT NULL;

INSERT INTO word_variations (base_word_id, variation_name, meaning, description) 
VALUES 
    (1, 'ombrengen', 'öldürmek', 'Biri için ölümüne sebep olmak anlamına gelir.'),
    (1, 'afbrengen', 'caydırmak', 'Birini bir şey yapmaktan vazgeçirmek.');

INSERT INTO grammers (grammer_name, description) 
VALUES 
    ('Perfectum', 'Geçmiş zaman çekimi için kullanılır.'),
    ('Futurum', 'Gelecek zamanı ifade eder.');
SELECT * 
FROM grammers;

INSERT INTO user_words (user_id, word_id, dutch_sentence, turkish_sentence) 
VALUES 
    (1, 1, 'Ik breng mijn broer naar school.', 'Kardeşimi okula götürüyorum.'),
    (2, 2, 'Mijn huis is groot.', 'Benim evim büyük.');
SELECT * 
FROM user_words;

-- Kullanıcının çalıştığı kelimeleri ve cümleleri göster
SELECT u.username, w.word_name, uw.dutch_sentence, uw.turkish_sentence
FROM user_words uw
JOIN users u ON uw.user_id = u.user_id
JOIN words w ON uw.word_id = w.word_id;

UPDATE users
SET password = 'a'
WHERE role = 'admin';

UPDATE users
SET password = 'b'
WHERE role = 'user';

CREATE TABLE word_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(20) UNIQUE NOT NULL CHECK (type_name IN ('verb', 'noun', 'adjective', 'adverb'))
);

INSERT INTO word_types (type_name) VALUES ('verb'), ('noun'), ('adjective'), ('adverb');

-- tablodaki sutunu degistirme
ALTER TABLE words DROP COLUMN word_type;
ALTER TABLE words ADD COLUMN type_id INT REFERENCES word_types(type_id) ON DELETE CASCADE;

SELECT * 
FROM word_types;

--words tablosundaki eski kayıtlara uygun type_id atayalım:
UPDATE words SET type_id = (SELECT type_id FROM word_types WHERE type_name = 'verb') WHERE word_name = 'brengen';
UPDATE words SET type_id = (SELECT type_id FROM word_types WHERE type_name = 'noun') WHERE word_name = 'huis';

INSERT INTO words (word_name, meaning, description, type_id) VALUES
-- 🟢 40 Fiil (Werkwoorden)
('werken', 'çalışmak', 'Bir işi yapmak veya mesleğini icra etmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('leren', 'öğrenmek', 'Yeni bilgi edinmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('schrijven', 'yazmak', 'Harf ve kelimeleri kağıda veya dijital ortama aktarmak.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('spreken', 'konuşmak', 'Bir dilde kelimeleri sesli olarak söylemek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('kopen', 'satın almak', 'Bir şey için para ödemek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('verkopen', 'satmak', 'Bir şeyi başka birine para karşılığı vermek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('eten', 'yemek yemek', 'Gıda tüketmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('drinken', 'içmek', 'Bir sıvıyı ağzına alarak yutmak.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('rijden', 'sürmek', 'Araba, bisiklet veya başka bir taşıtı kullanmak.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('lopen', 'yürümek', 'Ayaklarını sırayla hareket ettirerek ilerlemek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('zwemmen', 'yüzmek', 'Suda hareket etmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('slapen', 'uyumak', 'Gözleri kapatarak dinlenmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('wachten', 'beklemek', 'Bir olayın gerçekleşmesini sabırla beklemek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('vragen', 'sormak', 'Bir şey hakkında bilgi edinmek istemek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('antwoorden', 'cevap vermek', 'Bir soruya yanıt vermek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('beginnen', 'başlamak', 'Bir şeye başlamak veya girişmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('stoppen', 'durmak', 'Bir eylemi sonlandırmak.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('begrijpen', 'anlamak', 'Bir şeyi kavramak veya idrak etmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('denken', 'düşünmek', 'Zihinde fikir üretmek.', (SELECT type_id FROM word_types WHERE type_name = 'verb')),
('geloven', 'inanmak', 'Bir şeyin doğru olduğunu kabul etmek.', (SELECT type_id FROM word_types WHERE type_name = 'verbl')),

-- 🔵 40 İsim (Zelfstandige Naamwoorden)
('huis', 'ev', 'Yaşanılan yapı, konut.', (SELECT type_id FROM word_types WHERE type_name = 'noun')),
('auto', 'araba', 'Motorlu kara taşıtı.', (SELECT type_id FROM word_types WHERE type_name = 'noun')),
('school', 'okul', 'Eğitim verilen yer.', (SELECT type_id FROM word_types WHERE type_name = 'noun')),
('werk', 'iş', 'Meslek veya uğraş.', (SELECT type_id FROM word_types WHERE type_name = 'noun')),
('boek', 'kitap', 'Okumak için yazılmış eser.', (SELECT type_id FROM word_types WHERE type_name = 'noun')),
('tafel', 'masa', 'Üzerine nesneler konulan mobilya.', (SELECT type_id FROM word_types WHERE type_name = 'noun')),

-- 🟠 40 Sıfat (Bijvoeglijke Naamwoorden)
('groot', 'büyük', 'Boyut olarak geniş veya iri.', (SELECT type_id FROM word_types WHERE type_name = 'adjective')),
('klein', 'küçük', 'Boyut olarak küçük veya minik.', (SELECT type_id FROM word_types WHERE type_name = 'adjective')),
('mooi', 'güzel', 'Görünüm olarak hoş.', (SELECT type_id FROM word_types WHERE type_name = 'adjective')),
('lelijk', 'çirkin', 'Görünüm olarak hoş olmayan.', (SELECT type_id FROM word_types WHERE type_name = 'adjective')),
('nieuw', 'yeni', 'Daha önce kullanılmamış.', (SELECT type_id FROM word_types WHERE type_name = 'adjective')),
('oud', 'eski', 'Zaman içinde yaşlanmış.', (SELECT type_id FROM word_types WHERE type_name = 'adjective')),

-- 🟣 40 Zarf (Bijwoorden)
('snel', 'hızlı', 'Kısa sürede gerçekleşen.', (SELECT type_id FROM word_types WHERE type_name = 'adverb')),
('langzaam', 'yavaş', 'Uzun sürede gerçekleşen.', (SELECT type_id FROM word_types WHERE type_name = 'adverb')),
('vaak', 'sık sık', 'Çok kez olan.', (SELECT type_id FROM word_types WHERE type_name = 'adverb')),
('nooit', 'hiç', 'Bir kez bile olmayan.', (SELECT type_id FROM word_types WHERE type_name = 'adverb')),
('soms', 'bazen', 'Ara sıra gerçekleşen.', (SELECT type_id FROM word_types WHERE type_name = 'adverb')),
('altijd', 'her zaman', 'Sürekli gerçekleşen.', (SELECT type_id FROM word_types WHERE type_name = 'adverb'));
SELECT * 
FROM words;
