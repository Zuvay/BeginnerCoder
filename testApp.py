import mysql.connector
from connectionInfo import user, host, password, database
import matplotlib.pyplot as plt
import numpy as np

class Who5Test:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(f"Hata: {err}")

        self.answers = []

    def get_questions(self):
        query = "SELECT questionary FROM testdatabase.`who-5-test-questionary`;"
        self.cursor.execute(query)
        questions = self.cursor.fetchall()
        return [question[0] for question in questions]

    def display_question(self, question, index):
        print(f"{index + 1}. {question}")
        print("   5: Her zaman")
        print("   4: Çoğu zaman")
        print("   3: Geçen zamanın yarısından fazla")
        print("   2: Geçen zamanın yarısından az")
        print("   1: Bazen")
        print("   0: Hiçbir zaman")

    def get_user_answer(self):
        while True:
            try:
                answer = int(input("Cevabınızı girin (0-5): "))
                if 0 <= answer <= 5:
                    return answer
                else:
                    print("Geçersiz giriş. Lütfen 0-5 arasında bir değer girin.")
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")

    def start_test(self):
        questions = self.get_questions()

        for index, question in enumerate(questions):
            self.display_question(question, index)
            user_answer = self.get_user_answer()
            self.answers.append(user_answer)
        
        total_score = sum(self.answers)
        print("Test tamamlandı. Puanınız:", total_score)
        self.save_score_to_database(total_score)


    def save_score_to_database(self, total_score):
        try:
            # Mevcut total_score'u al ve yeni puanı ekleyerek güncelle
            update_query = "INSERT INTO `testdatabase`.`who_5_scores` (`scores`) VALUES (%s)"
            self.cursor.execute(update_query, (total_score,))

            self.connection.commit()
            print("Puan başarıyla kaydedildi.")
        except mysql.connector.Error as err:
            print(f"Hata: {err}")

    @staticmethod
    def getGraphic():
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            cursor = connection.cursor()

            # Veritabanından al
            select_query = "SELECT scores FROM who_5_scores"
            cursor.execute(select_query)
            scores = [int(score[0]) for score in cursor.fetchall()]

            # Çizgi grafiği
            plt.plot(np.arange(1, len(scores) + 1), scores, marker='o', linestyle='-')

            # Eksenler
            plt.title('WHO 5 Test Grafiği')
            plt.xlabel('Çözülen test sayısı')
            plt.ylabel('Alınan Test Puanları')
            
            # X ekseni değerlerini belirleme
            x_values = np.arange(1, len(scores) + 1)
            plt.xticks(x_values, map(str, x_values))

            # Y ekseni değerlerini belirleme
            max_y_value = max(scores) + 5
            y_ticks = np.arange(0, max_y_value, step=5)
            plt.yticks(y_ticks, map(str, y_ticks))

            plt.show()

        except mysql.connector.Error as err:
            print(f"Hata: {err}")
        finally:
            cursor.close()
            connection.close()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

#Who-5 test, başlat
who5_test = Who5Test(host, user, password, database)
who5_test.start_test()
who5_test.close_connection()

#SQL'den verileri alıp grafiğe dökmek için static metot
#Who5Test.getGraphic()

