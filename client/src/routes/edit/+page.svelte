<script lang="ts">
	import { goto } from "$app/navigation";
	import { updateImageDataStatus } from "../../apis";

    let imageName: string = '';
    let imageStatus: string = '';
    let error: string = '';

    const handleSubmit = async (event: Event) =>{
        event.preventDefault();
        if (!imageName) {
			error = 'Image Name field is required';
		} else if (!imageStatus) {
			error = 'Image Status field is required';
		}else{
            try{
                const response = await updateImageDataStatus(imageName, imageStatus);
                if(response.imageData){
                    goto('/profile');
                }else{
                    error = response.error || 'Empty error message was by the server';
                }
            }catch(e){
                error = 'Ooops, something went wrong';
                console.log(e)
            }
        }
    };
</script>


{#if error !== ''}
	<p style="color:red">{error}</p>
{/if}
<form on:submit={handleSubmit}>
    <div>
        <label for="imageName">Image Name:</label>
        <input type="text" id="imageName" bind:value={imageName} />
    </div>

    <div>
        <label for="imageStatus">Image Status:</label>
        <input type="text" id="imageStatus" bind:value={imageStatus} />
    </div>
    <div>
        <button type="submit">Edit</button> 
    </div>
</form>
