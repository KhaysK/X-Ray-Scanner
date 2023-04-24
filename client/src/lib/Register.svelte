<script lang="ts">
	import { loginToggle } from '../stores';
	import { goto } from '$app/navigation';
	import { register, setUser } from '../apis';
	import { base } from '$app/paths';

	let username: string = '';
	let password: string = '';
	let confirmPassword: string = '';
	let error: string = '';

	const handleSubmit = async (event: Event) => {
		event.preventDefault();

		if (!username) {
			error = 'Username field is required';
		} else if (!password) {
			error = 'Password field is required';
		} else if (!confirmPassword) {
			error = 'Confirm Password field is required';
		} else if (password !== confirmPassword) {
			error = 'Passwords do not match';
		} else {
			try {
				const response = await register(username, password, confirmPassword);
				if (response.username) {
					setUser({ username: response.username });
					loginToggle.set('');
					username = '';
					password = '';
					confirmPassword = '';
					goto(`${base}/`);
				} else {
					error = response.error || 'Empty error message was sent by the server';
				}
			} catch (e) {
				error = 'Ooops, something went wrong';
				console.log(e);
			}
		}
	};
</script>

<div id="container">
	<div id="closeBtn" on:click={() => loginToggle.set('')}>X</div>

	<div style="text-align: center;">
		<h1>Registration</h1>
		{#if error !== ''}
			<p style="color:red">{error}</p>
		{/if}
	</div>

	<form on:submit={handleSubmit}>
		<div>
			<label for="username">Username:</label>
			<input type="text" id="username" bind:value={username} />
		</div>

		<div>
			<label for="password">Password:</label>
			<input type="password" id="password" bind:value={password} />
		</div>
		<div>
			<label for="confirm">Confirm:</label>
			<input type="password" id="confirm" bind:value={confirmPassword} />
		</div>
		<div>
			<button on:click={() => loginToggle.set('Login')}>Login</button>
			<button type="submit">Register</button>
		</div>
	</form>
</div>

<style>
	#container {
		position: absolute;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 16px;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		width: 500px;
		height: 300px;
		border: 2px solid #22577a;
		border-radius: 10px;
		background-color: #f3f0ec;
	}

	form {
		display: flex;
		justify-content: space-between;
		align-items: center;
		flex-direction: column;
		font-size: 32px;
		width: 100%;
		height: 300px;
	}

	input {
		font-size: 16px;
	}

	button {
		border: 1px solid #22577a;
		border-radius: 8px;
		width: 120px;
		height: 45px;
		font-size: 18px;
		margin-bottom: 16px;
	}

    #closeBtn{
        display: block;
        position: absolute;
        top: 0;
        right: 0;
        color: red;
        font-size: 22px;
        font-family: Arial, Helvetica, sans-serif;
        margin: 10px;
    }

</style>
