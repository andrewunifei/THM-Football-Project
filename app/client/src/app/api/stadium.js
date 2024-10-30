export async function getTopStadiums() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/stadiums/top', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}

export async function getBottomStadiums() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/stadiums/bottom', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}

export async function getCapacitiesData() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/stadiums/capacities-categorized', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
}

export async function getSurfaceData() {
    const options = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }
    try {
        const response = await fetch('http://127.0.0.1:5000/stadiums/surface-occurrences', options)
        const parsed = await response.json()
        return parsed
    }
    catch(e) {
        console.log(e)
    }
} 