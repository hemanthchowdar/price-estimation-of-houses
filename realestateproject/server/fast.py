from fastapi import FastAPI

app=FastAPI()
food_items={
    "indian":['Samosa',"Dosa"],
    "american":['Hot Dog','Apple pie'],
    "italian":['Ravoli','pizza']
}
@app.get('/get_food/{cusine}')
async def get_food(cusine):
    if cusine not in food_items.keys():
        return 'only validate cusine are indian,american,italian'
    return food_items.get(cusine)
