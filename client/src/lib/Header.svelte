<script lang="ts">
	import { page } from '$app/stores';
	import { base } from '$app/paths';
	import { onDestroy, onMount } from 'svelte';
	import { clearUser, getUser, setUser } from '../apis';
	import { user, loginToggle } from '../stores';

	$: routeId = $page.route.id;

	let username = '';
    
	const unsubscribe = user.subscribe((value) => {
		if (!value) {
			username = '';
		} else {
			username = value.username;
		}
	});

	onMount(async () => {
		setUser(await getUser());
	});
	onDestroy(unsubscribe);
</script>

<div id="navbar">
	<div id="logo">X-SCAN</div>
	<div id="links-container">
		<a href="{base}/" class:active={routeId == '/'}>Lung X-Ray</a>
		<a href="{base}/soon" class:active={routeId == '/soon'}>Coming Soon</a>
	</div>
	{#if !username}
		<a href="#" on:click={() => (loginToggle.set('Login'))}>
			<div id="profile">Login</div>
		</a>
	{:else if routeId == '/profile' || routeId == '/profile/'}
		<a href="{base}/" on:click={clearUser}>
			<div id="profile">Logout</div>
		</a>
	{:else}
		<a href="{base}/profile">
			<div id="profile">{username}</div>
		</a>
	{/if}
</div>

<style>
	#navbar {
		min-height: 70px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 64px;
		padding: 0 4rem;
		flex-shrink: 0;
		color: #22577a;
		background-color: #fff;
		z-index: 5;
		font-size: 24px;
		-webkit-box-shadow: 0px 7px 10px -1px rgba(34, 60, 80, 0.2);
		-moz-box-shadow: 0px 7px 10px -1px rgba(34, 60, 80, 0.2);
		box-shadow: 0px 7px 10px -1px rgba(34, 60, 80, 0.2);
	}

	#links-container {
		display: flex;
		flex: 1;
		font-size: 24px;
		font-weight: bold;
		justify-content: center;
		gap: 24px;
	}

	#logo {
		font-size: 32px;
		font-weight: bold;
	}

	.active {
		color: #57cc99;
	}

	#profile {
		background-color: #f3f0ec;
		height: 100%;
		width: 110px;
		line-height: 70px;
		text-align: center;
		font-weight: bold;
	}

	#profile:hover {
		background-color: #c7f9cc;
	}
</style>
