export async function getGamesCategorized(year, month) {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch(`http://127.0.0.1:5000/games/categorized?year=${year}&month=${month}`, options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}

export async function getGamesAvailable() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/games/available', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}

export async function getGameDetails(game_id) {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch(`http://127.0.0.1:5000/games/details?game-id=${game_id}`, options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}