CREATE TABLE users (
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	password TEXT NOT NULL,
	role VARCHAR(10) CHECK (role IN ('admin', 'user')) NOT NULL
);

CREATE TABLE words (
	word_id SERIAL PRIMARY KEY,
	word_name VARCHAR(50) NOT NULL,
	word_type VARCHAR(20) NOT NULL CHECK (word_type IN ('fiil', 'isim', 'sıfat', 'zarf')) NOT NULL,
	meaning VARCHAR(100) NOT NULL,
	description TEXT
	
);

CREATE TABLE word_variations(
	variation_id SERIAL PRIMARY KEY,
	base_word_id INT REFERENCES words(word_id) ON DELETE CASCADE,
	variation_name VARCHAR(50) NOT NULL,
	meaning VARCHAR(100) NOT NULL,
	description TEXT
);

CREATE TABLE grammers(
	grammer_id SERIAL PRIMARY KEY,
	grammer_name VARCHAR(150) NOT NULL,
	description TEXT
);

CREATE TABLE user_words(
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
	word_id INT REFERENCES words(word_id) ON DELETE CASCADE,
	dutch_sentence TEXT,
	turkish_sentence TEXT,
	date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
