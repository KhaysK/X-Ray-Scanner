<script lang="ts">
    import {login, setUser} from '../../apis'
	import { goto } from '$app/navigation';

    let username: string = '';
    let password: string = '';
    let error: string = '';

    const handleSubmit = async (event: Event) =>{
        event.preventDefault();

        try{
            const response = await login(username, password);
            if(response.username){
                setUser({'username': response.username});
                goto('/profile');
            }else{
                error = response.error || 'Empty error message was by the server';
            }
        }catch(e){
            error = 'Ooops, something went wrong';
            console.log(e)
        }
    };

</script>


<h1>Login</h1>

{#if error !== ''}
    <p style="color:red">{error}</p>
{/if}

<form on:submit={handleSubmit}>
    <label for="username">Username:</label>
    <input type="text" id = "username" bind:value={username}/>

    <label for="password">Password:</label>
    <input type="password" id="password" bind:value={password}/>

    <button type="submit">Log In</button>
</form>
