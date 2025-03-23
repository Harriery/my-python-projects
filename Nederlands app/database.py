import psycopg2
import bcrypt  # Şifreleri güvenli kıyaslamak için

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
def check_username(username, password):
    conn = connect_to_db()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            hashed_password = user[0]  # Veritabanından gelen hash
            return bcrypt.checkpw(password.encode(), hashed_password.encode())  # Şifreyi doğrula
        return False  # Kullanıcı bulunamadıysa False dön
    except Exception as e:
        print(f"Sorgu hatası: {e}")
        return False

def get_words():
    conn = connect_to_db()
    if not conn:
        return None  # Bağlantı kurulamazsa None dön

    try:    
        cursor = conn.cursor()
        query = "SELECT * FROM words"
        cursor.execute(query)
        words = cursor.fetchall()  # Sonucu al

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
