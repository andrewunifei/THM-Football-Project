export async function getPlayersCategorized() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/players/categorized', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}

export async function getPlayerInfo(player_id) {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch(`http://127.0.0.1:5000/players/player-info?player-id=${player_id}`, options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}