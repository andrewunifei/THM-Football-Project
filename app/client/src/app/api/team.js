export async function getTeamsInfo() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/teams-info', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}

export async function getTeamsGamesInfo(code) {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch(`http://127.0.0.1:5000/teams-games-info?code=${code}`, options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}