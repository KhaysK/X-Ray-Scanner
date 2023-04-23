<script lang="ts">
	import { goto } from "$app/navigation";
	import { register, setUser } from "../../apis";
    import { base } from "$app/paths";

    let username: string = '';
    let password: string = '';
    let confirmPassword: string = '';
    let error: string = '';

    const handleSubmit = async (event: Event) =>{
        event.preventDefault();
        
        if (password !== confirmPassword){
            error = 'Passwords do not match';
        }

        try{
            const response = await register(username, password, confirmPassword);
            if (response.username){
                setUser({'username': response.username});
                goto(`${base}/`);
            }else{
                error = response.error || 'Empty error message was sent by the server'
            }
        }catch(e){
            error = 'Ooops, something went wrong';
            console.log(e);
        }
    }


    
</script>


{#if error !== ''}
    <p style="color:red">{error}</p>
{/if}

<form on:submit={handleSubmit}>
    <label for="username">Username:</label>
    <input type="text" bind:value={username}>

    <label for="password">Password:</label>
    <input type="password" bind:value={password}>

    <label for="confirm password">Confirm Password</label>
    <input type="password" bind:value={confirmPassword}>

    <button type="submit">Register</button>
</form>