<script lang="ts">
    import { onMount } from 'svelte';

    let fileSelector: HTMLInputElement;
    let fileDragger: HTMLDivElement;
    let fileName: string;

    onMount(() => {
        fileSelector = document.getElementById('fileSelector') as HTMLInputElement;
        fileDragger =  document.getElementById('container') as HTMLDivElement;

        fileSelector.addEventListener('change', function(e){
            let file = this.files?.[0] as File;
            uploadFileHandler(file);
        });
        
        fileDragger.addEventListener('dragover', (e) => {
            e.preventDefault();
            console.log("over");
        });  

        fileDragger.addEventListener('drop', (e) => {
            e.preventDefault();
            let file = e.dataTransfer?.files[0] as File;
            uploadFileHandler(file);
        });  
    });

    function uploadFileHandler(file: File){
        console.log(file);
        fileName = file.name
    }
</script>

<div id="container">
    <div id="titleInfo">
        <h1>Lung X-Ray</h1>
        <span>Determines the presence of lung inflammation by X-ray image</span>
    </div>
    <input type="file" id="fileSelector" accept="image/*" hidden/>
    <label for="fileSelector">Select File</label>
    <span style="margin-top: -90px; text-align:center;">Or Drag and Drop it <br>{fileName}</span>
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
    label{
        height: 6rem;
        width: 22rem;
        border: none;
        border-radius: 10px;
        background-color: #57cc99;
        color: #f3f0ec;
        font-size: 36px;
        text-align: center;
        line-height: 6rem;
        transition: all 0.2s ease-in;
    }
    label:hover{
        background-color: #38a3a5;
    }
</style>