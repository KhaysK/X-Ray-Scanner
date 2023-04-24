<script lang="ts">
	import { goto } from '$app/navigation';
    import { user } from '../../stores';
	import { onMount } from 'svelte';
    import { page } from '$app/stores';
    import { history } from '../../apis';
	import { onDestroy } from 'svelte';
    import { base } from '$app/paths';
    
    $: username = $user?.username; 
    $: message = `Welcome ${username}`;

    let imageDatas: ImageData[] = [];


    const unsubscribe = page.subscribe(async (value)=>{
        try{
            const response = await history();
            if (response.imageDatas){
                imageDatas = response.imageDatas;
            }
        }catch(e){
            console.log(`ERROR:${e}`);
        }
    });

    onMount(()=>{
        if( username === undefined){
            goto('/');
        }
    });

    onDestroy(unsubscribe);

</script>

<div class="just-fixed">
    <h1>{message}</h1>
    <a href="{base}/edit" style="font-size:30px">Edit</a>
    <ul>
        {#each imageDatas as imageData}
            <li>
                <p>Name: {imageData.name}</p>
                <p>Extension: {imageData.ext}</p>
                <p>Result: {imageData.result}</p>
                <p>Created at: {imageData.created_at}</p>
                <p>Username: {imageData.username}</p>
                <p>Status: {imageData.status}</p>
            </li>
        {/each}
    </ul>
</div>


<style>
    .just-fixed {
		background-color: #f1f1f1;
		position: fixed;
		top: 80px;
		left: 300px;
    }
</style>