import sqlite3
#queries string mai(single'',double""), triple also allowed and usse formatting same rehti hai jo bhi ''' ''' mai ho uski jo jaise likha waise ka waise feed hota hai

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)
               ''') 

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print("Empty DB")
        
    else:
        for row in videos:
            print(row)

        

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name= ?, time= ? WHERE id=?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()
    

def main():
    while True:
        print("\n Youtube Manager with sqlite3 by Veer Shah")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit Youtube Manager")
        choice=input("Enter your choice: ")
    
        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video id: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id,name,time)
            case '4':
                video_id = input("Enter the video id: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__=="__main__":
    main()

