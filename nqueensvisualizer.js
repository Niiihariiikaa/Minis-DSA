const N = 8;
let board = new Array(N).fill(-1);
let gameActive = true;

document.addEventListener("DOMContentLoaded", () => {
    const appContainer = document.createElement("div");
    appContainer.id = "app";
    appContainer.style.display = "flex";
    appContainer.style.flexDirection = "column";
    appContainer.style.alignItems = "center";
    document.body.appendChild(appContainer);
    
    const title = document.createElement("h1");
    title.innerText = "N-Queens Game";
    appContainer.appendChild(title);
    
    const boardContainer = document.createElement("div");
    boardContainer.id = "board";
    boardContainer.style.display = "grid";
    boardContainer.style.gridTemplateColumns = `repeat(${N}, 60px)`;
    boardContainer.style.gridTemplateRows = `repeat(${N}, 60px)`;
    boardContainer.style.gap = "2px";
    boardContainer.style.marginTop = "20px";
    boardContainer.style.backgroundColor = "#4CAF50";
    appContainer.appendChild(boardContainer);
    
    const restartButton = document.createElement("button");
    restartButton.innerText = "Restart Game";
    restartButton.style.marginTop = "20px";
    restartButton.onclick = resetGame;
    appContainer.appendChild(restartButton);
    
    const style = document.createElement("style");
    style.innerHTML = `
        .cell {
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid black;
            font-size: 24px;
            cursor: pointer;
            background-color: rgba(255, 255, 255, 0.8);
        }
        .queen {
            width: 50px;
            height: 50px;
            background-image: url('https://upload.wikimedia.org/wikipedia/commons/4/49/Chess_qdt45.svg');
            background-size: cover;
        }
        .message {
            font-size: 18px;
            margin-top: 10px;
            color: yellow;
        }
    `;
    document.head.appendChild(style);
    
    drawBoard();
});

function drawBoard() {
    const container = document.getElementById("board");
    container.innerHTML = "";
    for (let row = 0; row < N; row++) {
        for (let col = 0; col < N; col++) {
            const cell = document.createElement("div");
            cell.className = "cell";
            cell.onclick = () => placeQueen(row, col);
            if (board[row] === col) {
                const queen = document.createElement("div");
                queen.className = "queen";
                cell.appendChild(queen);
            }
            container.appendChild(cell);
        }
    }
}

function placeQueen(row, col) {
    if (!gameActive) return;
    if (isSafe(row, col)) {
        board[row] = col;
        drawBoard();
        if (board.every(pos => pos !== -1)) {
            gameActive = false;
            displayMessage("Congratulations! You solved the puzzle.");
        }
    } else {
        displayMessage("Invalid move! Queens cannot attack each other.");
    }
}

function isSafe(row, col) {
    for (let i = 0; i < row; i++) {
        if (board[i] === col || Math.abs(board[i] - col) === Math.abs(i - row)) {
            return false;
        }
    }
    return true;
}

function resetGame() {
    board.fill(-1);
    gameActive = true;
    drawBoard();
    displayMessage("");
}

function displayMessage(msg) {
    let messageBox = document.getElementById("message");
    if (!messageBox) {
        messageBox = document.createElement("div");
        messageBox.id = "message";
        messageBox.className = "message";
        document.getElementById("app").appendChild(messageBox);
    }
    messageBox.innerText = msg;
}
