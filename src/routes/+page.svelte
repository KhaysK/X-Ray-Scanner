<div id="container">
    <div id="titleInfo">
        <h1>Lung X-Ray</h1>
        <div>Determines the presence of lung inflammation by X-ray image</div>
    </div>
    <button>Select File</button>
</div>

<style>
    #container{
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        gap: 96px;
        align-items: center;
        background-color: #f3f0ec;
        color: #22577A;
        font-size: 24px;
    }
    #titleInfo{
        display: flex;
        flex-direction: column;
        justify-content: flex-start;  
        align-items: center;
    }
    button{
        height: 6rem;
        width: 22rem;
        border: none;
        border-radius: 10px;
        background-color: #57cc99;
        color: #f3f0ec;
        font-size: 36px;
        transition: all 0.2s ease-in;
    }
    button:hover{
        background-color: #38a3a5;
    }
</style>