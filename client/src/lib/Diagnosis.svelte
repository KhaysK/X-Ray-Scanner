<script lang="ts">
	export let imagePath: string;
	export let patientName: string;
	export let date: string;
	export let diagnosis: string;
	export let status: string;
	import { updateImageDataStatus } from '../apis';
	import { user } from '../stores';

	let error: string = '';
	$: username = $user?.username;

	async function changeStatus(imageStatus: string) {
		try {
			const response = await updateImageDataStatus(imagePath, imageStatus);
			if (response.imageData) {
				status = imageStatus;
			} else {
				error = response.error || 'Empty error message was by the server';
			}
		} catch (e) {
			error = 'Ooops, something went wrong';
			console.log(e);
		}
	}
</script>

<div id="container">
	<img src={`/api/get/image/${imagePath}`} alt="Xray" width="200px" />
	<div id="info">
		{#if error !== ''}
			<p style="color:red">{error}</p>
		{/if}
		<p>Patient: {patientName}</p>
		<p>Date: {date}</p>
		<p>Diagnosis: {diagnosis}</p>
		<p>Status: {status}</p>
		{#if username == 'admin'}
			<div>
				<button
					style="background-color: #5cbf2a;"
					on:click|preventDefault={() => {
						changeStatus('approved');
					}}>Approve</button
				>
				<button
					style="background-color: red;"
					on:click|preventDefault={() => {
						changeStatus('declined');
					}}>Decline</button
				>
			</div>
		{/if}
	</div>
</div>

<style>
	#container {
		width: 600px;
		height: 350px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		background-color: #f3f0ec;
		color: #22577a;
		border: 2px solid #22577a;
		border-radius: 10px;
		padding: 20px;
	}

	#info {
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		height: 100%;
		font-size: 18px;
	}

	button {
		border: 1px solid #22577a;
		border-radius: 8px;
		width: 120px;
		height: 45px;
		font-size: 18px;
		margin-bottom: 16px;
	}

	button:active {
		position: relative;
		top: 1px;
	}
</style>
