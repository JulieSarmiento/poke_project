/* Fetch data function to help error handling */
export async function fetchData<T>(url:string): Promise<T> {
    const response = await fetch(url);

    if(!response.ok) {
        throw new Error(`Fetch failed: ${response.statusText}`)
    }

    return response.json();
}