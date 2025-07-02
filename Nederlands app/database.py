import psycopg2

# Veritabanına bağlanmak için fonksiyon
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="nederlands_leren",
            user="postgres",
            password="411.Falcon",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        return None

# Kullanıcı adı ve şifre kontrolü
def check_password(username, password):
    conn = connect_to_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user[0]  # Veritabanından gelen şifre (düz metin olarak saklandığını varsayıyoruz)
            return password == stored_password  # Düz metin karşılaştırması
        
        return False  # Kullanıcı bulunamadıysa False dön
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_words():
    conn = connect_to_db()
    if not conn:
        return None  # Bağlantı kurulamazsa None dön

    try:    
        cursor = conn.cursor()
        query = "SELECT * FROM words"
        cursor.execute(query)
        words = cursor.fetchall()  # Sonucu al
        print("Gelen veriler:", words)  # Test için
        return words  # Verileri döndür
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return None
    finally:
        cursor.close()
        conn.close()  # Her durumda bağlantıyı kapat

def get_word_types():
    conn = connect_to_db()
    if not conn:
        return None  # Bağlantı kurulamazsa None dön

    try:    
        cursor = conn.cursor()
        query = "SELECT * FROM word_types"
        cursor.execute(query)
        words = cursor.fetchall()  # Sonucu al

        return words  # Verileri döndür
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return None
    finally:
        cursor.close()
        conn.close()  # Her durumda bağlantıyı kapat

def get_word_variations():
    conn = connect_to_db()
    if not conn:
        return None  # Bağlantı kurulamazsa None dön

    try:    
        cursor = conn.cursor()
        query = "SELECT * FROM word_variations"
        cursor.execute(query)
        words = cursor.fetchall()  # Sonucu al

        return words  # Verileri döndür
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return None
    finally:
        cursor.close()
        conn.close()  # Her durumda bağlantıyı kapat

def check_username(username):
    conn = connect_to_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        
        return user is not None  # Kullanıcı varsa True, yoksa False dön
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_words_by_type(word_type_id):
    """Belirtilen kelime türüne ait kelimeleri getir"""
    conn = connect_to_db()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        query = "SELECT id, word FROM words WHERE type_id = %s"
        cursor.execute(query, (word_type_id))
        words = cursor.fetchall()
        conn.close()
        return words if words else []
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_word_variations_by_word(word_id):
    conn = connect_to_db()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        query = "SELECT variation_id, variation_name FROM word_variations WHERE word_id = %s"
        cursor.execute(query, (word_id))
        variations = cursor.fetchall()
        conn.close()
        return variations if variations else []
    
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
types = get_word_types()
print("Kelime Türleri:", types)