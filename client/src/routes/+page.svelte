<script lang="ts">
	import { getPrediction } from '../apis';
	import Login from '../lib/Login.svelte';
	import Register from '../lib/Register.svelte';
	import { loginToggle } from '../stores';

	let resultImg: HTMLImageElement;
	let resultTxt: HTMLParagraphElement;
	let isResultReady: boolean = false;

	function toggleReady() {
		isResultReady = !isResultReady;
	}

	function draggerHandler(event: DragEvent) {
		const files = event.dataTransfer?.files;
		if (files?.length) {
			const file = files[0];
			uploadFileHandler(file);
		}
	}

	function selectorHandler(event: Event) {
		const inputElement = event.target as HTMLInputElement;
		const file = inputElement.files?.[0] as File;

		if (!file) return;

		uploadFileHandler(file);
	}

	async function uploadFileHandler(file: File) {
		try {
			const prediction = await getPrediction(file);
			if (prediction.result) {
				if (!isResultReady) toggleReady();
				displayResult(file, prediction.result);
			} else {
				alert(`ERROR: ${prediction.error}`);
			}
		} catch (error) {
			console.error(`ERROR: ${error}`);
		}
	}

	function displayResult(file: File, result: string) {
		const reader = new FileReader();

		reader.onload = () => {
			resultImg.src = reader.result as string;
			resultTxt.textContent = `Result: ${result}`;
		};

		if (file) {
			reader.readAsDataURL(file);
		}
	}

	loginToggle.set('');
</script>

{#if $loginToggle == 'Login'}
	<Login />
{:else if $loginToggle == 'Register'}
	<Register />
{/if}

<div
	id="container"
	on:drop|preventDefault={(e) => draggerHandler(e)}
	on:dragover|preventDefault={() => {}}
>
	<div id="titleInfo">
		<h1>Lung X-Ray</h1>
		<span>Determines the presence of lung inflammation by X-ray image</span>
	</div>
	<input
		type="file"
		id="fileSelector"
		accept="image/*"
		on:change|preventDefault={(e) => selectorHandler(e)}
		hidden
	/>
	<label for="fileSelector">Select File</label>
	<span style="margin-top: -90px; text-align:center;">Or Drag and Drop it</span>
	{#if isResultReady}
		<div id="resultPanel">
			<img src="" alt="" bind:this={resultImg} />
			<p bind:this={resultTxt} />
		</div>
	{/if}
</div>

<style>
	#container {
		height: 100%;
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		gap: 96px;
		align-items: center;
		background-color: #f3f0ec;
		color: #22577a;
		font-size: 24px;
	}
	#titleInfo {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: center;
	}
	label {
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

	label:hover {
		background-color: #38a3a5;
	}

	#resultPanel {
		display: flex;
		flex-direction: row;
		align-items: center;
		margin-top: -60px;
	}

	img {
		width: 400px;
		height: 350px;
		margin-right: 20px;
		border-radius: 10px;
	}

	p {
		font-size: 24px;
		align-self: flex-start;
	}
</style>
