import sqlite3 as sql

conn = sql.connect(database="data.db" , check_same_thread=False)
c = conn.cursor()



def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS article_form_one(first_name TEXT , last_name TEXT , age INTEGER , gender TEXT , education TEXT , job TEXT , use_ai_for_academic_work TEXT , app_or_web TEXT , web_browser TEXT , iranian_site TEXT , foreign_site TEXT , why_use TEXT , another_reason TEXT , ai_ssp TEXT)")

def add_data(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work  , app_or_web , web_browser , iranian_site , foreign_site , why_use , another_reason , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , foreign_site , why_use , another_reason , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , foreign_site , why_use , another_reason , ai_ssp))
    conn.commit()

def add_data1(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work) VALUES (?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work))
    conn.commit()

def add_data2(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work  , app_or_web , web_browser , iranian_site , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , ai_ssp))
    conn.commit()
def add_data2_foreign(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work  , app_or_web , web_browser , foreign_site , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site , ai_ssp))
    conn.commit()
def add_data2_irf(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work  , app_or_web , web_browser ,iranian_site ,  foreign_site , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser ,iranian_site ,  foreign_site , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site,  foreign_site , ai_ssp))
    conn.commit()

def add_data3(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site, why_use , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , why_use , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , why_use , ai_ssp))
    conn.commit()
def add_data3_foreign(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site, why_use , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site , why_use , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site , why_use , ai_ssp))
    conn.commit()
def add_data3_irf(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser ,iranian_site ,  foreign_site, why_use , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser ,iranian_site ,  foreign_site , why_use , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser ,iranian_site ,  foreign_site , why_use , ai_ssp))
    conn.commit()

def add_data4(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , why_use , another_reason , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , why_use , another_reason , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , iranian_site , why_use , another_reason , ai_ssp))
    conn.commit()
def add_data4_foreign(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site , why_use , another_reason , ai_ssp):
    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site , why_use , another_reason , ai_ssp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , (first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , app_or_web , web_browser , foreign_site , why_use , another_reason , ai_ssp))
    conn.commit()


#def add_data2(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp):
#    c.execute(f"INSERT INTO article_form_one(first_name , last_name , age , gender , education , job ,  use_ai_for_academic_work , tool , app_or_web , web_browser , operating_system , why_use , another_reason , ai_ssp) VALUES ({first_name} , {last_name} , {age} , {gender} , {education} , {job} ,  {use_ai_for_academic_work} , {tool} , {app_or_web} , {web_browser} , {operating_system} , {why_use} , {another_reason} , {ai_ssp}) ")
#    conn.commit()

def view_all_data():
    c.execute("SELECT * FROM article_form_one")
    data = c.fetchall()
    return data

def view_unique_task():
    c.execute("SELECT DISTINCT first_name FROM article_form_one")
    data = c.fetchall()
    return data

def get_task(task):
    c.execute(f"SELECT * FROM article_form_one WHERE first_name='{task}'")
    data = c.fetchall()
    return data