const api_url = "http://127.0.0.1:5000/api/v1.0"


function options(method, json) {
    const opts = {
        "method": method,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        }
    }
    if (json != undefined) { 
        opts.headers["Content-Type"] = "application/json"
        opts.body = JSON.stringify(json)
    }
    return opts
}

export async function all_lists() {
    const rep = await fetch(`${api_url}/list`, options("GET"))
    const json = await rep.json()
    return json
}

export async function get_list(id) {
    const rep = await fetch(`${api_url}/list/${id}`, options("GET"))
    const json = await rep.json()
    return json
}

export async function add_list(json) {
    const rep = await fetch(`${api_url}/list`,
        options("POST", json)
    )
    json = await rep.json()
    return json
}

export async function del_list(id) {
    const rep = await fetch(`${api_url}/list/${id}`,
        options("DELETE")
    )
}

export async function modify_list(id, json) {
    const rep = await fetch(`${api_url}/list/${id}`,
        options("PUT", json)
    )
}


export async function get_item(id) {
    const rep = await fetch(`${api_url}/item/${id}`, options("GET"))
    const json = await rep.json()
    return json
}

export async function add_item(list_id, json) {
    json["list_id"] = list_id
    const rep = await fetch(`${api_url}/item`,
        options("POST", json)
    )
    json = await rep.json()
    return json
}

export async function del_item(id) {
    const rep = await fetch(`${api_url}/item/${id}`,
        options("DELETE")
    )
}

export async function modify_item(id, json) {
    const rep = await fetch(`${api_url}/item/${id}`,
        options("PUT", json)
    )
}