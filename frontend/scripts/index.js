async function makeSentence(text) {
    const request = await fetch("http://localhost:5000/generate", {
        method: "POST",
        headers: {
            'Content-Type': "application/json"
        },
        body: JSON.stringify({ text })
    })

    const response = await request.json();

    const words = Object.keys(response);
    let word = words[Math.floor(Math.random() * words.length)];
    let result = "";

    for (let i = 0; i < words.length; i++) {
        result += word + ' ';
        let newWord = response[word][Math.floor(Math.random() * response[word].length)];
        word = newWord;

        if (!word || !response.hasOwnProperty(word)) {
            word = words[Math.floor(Math.random() * words.length)];
        }
    }

    return result;
}

async function generateMarkov() {
    const input = document.getElementById("markov-input");
    const output = document.getElementById("markov-output");

    const result = await makeSentence(input.value);

    output.innerText = result;
} 