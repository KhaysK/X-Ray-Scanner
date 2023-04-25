<script lang="ts">
	import { goto } from '$app/navigation';
	import { user } from '../../stores';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { history } from '../../apis';
	import { onDestroy } from 'svelte';
	import Diagnosis from '../../lib/Diagnosis.svelte';

	$: username = $user?.username;
	$: message = `Welcome ${username}`;

	let imageDatas: ImageData[] = [];

	const unsubscribe = page.subscribe(async (value) => {
		try {
			const response = await history();
			if (response.imageDatas) {
				imageDatas = response.imageDatas;
			}
		} catch (e) {
			console.log(`ERROR:${e}`);
		}
	});

	onMount(() => {
		if (username === undefined) {
			goto('/');
		}
	});

	onDestroy(unsubscribe);
</script>

<div class="container">
	{#each imageDatas as imageData}
		<Diagnosis
			imagePath={imageData.name}
			patientName={imageData.username}
			date={imageData.created_at}
			diagnosis={imageData.result}
			status={imageData.status}
		/>
	{/each}
</div>

<style>
	.container {
		background-color: #f1f1f1;
		border: none;
		display: flex;
		align-items: center;
		height: 100%;
		width: 100%;
		flex-direction: column;
		overflow: auto;
		padding: 60px 0;
		gap: 16px;
	}
</style>
