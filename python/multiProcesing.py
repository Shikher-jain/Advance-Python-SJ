import multiprocessing
import requests

def downloadFile(url,name):
    print(f"{name} start")
    response=requests.get(url)
    open(f"{name}.png","wb").write(response.content)
    print(f"{name} finish")
    
if __name__=="__main__":
    urls="https://unsplash.com/photos/man-person-standing-between-tall-trees-F_-0BxGuVvo"
    pros=[]
    for i in range(5):
        # downloadFile(urls,f"MAN{i}")

        p=multiprocessing.Process(target=downloadFile,args=[urls,i])
        p.start()
        pros.append(p)

        for p in pros:
            p.join()  