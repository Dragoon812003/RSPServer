let data = {
    "distance": 78.4584454,
}

data = JSON.stringify(data)

parsedData = JSON.parse(data)
ultraSonicDist = parsedData.distance
console.log(`${ultraSonicDist.toFixed(2)}mm`)