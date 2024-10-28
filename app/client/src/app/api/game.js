export async function getGamesCategorized() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/games/categorized', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}