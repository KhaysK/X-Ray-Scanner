import {user} from './stores'

export async function login(username: string, password: string): Promise<LoginResponse>{
    const response = await fetch('/api/login',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    });

    const data: LoginResponse = await response.json();
    return data;
}


export async function register(username: string, password: string, confirmPassword: string): Promise<RegisterResponse>{
    const response = await fetch('/api/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password, confirmPassword})
    });
    
    const data: RegisterResponse = await response.json();
    return data;
}

export async function history(): Promise<HistoryResponse>{
    const response = await fetch('/api/history');

    const data: HistoryResponse = await response.json();
    return data;
}


export async function updateImageDataStatus(imageName: string, imageStatus: string): Promise<UpdateImageDataResponse>{
    const response = await fetch('/api/update/image', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            'image_name': imageName,
            'image_status': imageStatus
        })
    });

    const data: UpdateImageDataResponse = await response.json();
    return data;
}

export async function getUser(): Promise<User | null>{
    try{
        const response = await fetch('/api/getuser');
        
        if (response.ok){
            const data: User = await response.json();
            return data;
        }else{
            throw new Error(`Status:${response.status}; Error: ${response.statusText} `);
        }
    }catch(error){
        console.error(`ERROR: ${error}`);
    }

    return null;
}


export function setUser(newUser: User | null){
    user.update(x=>newUser);
}


export async function clearUser(){
    await fetch('/api/logout');
    setUser(null);
}


export async function getPrediction(file: File): Promise<PredictionResult>{
    const formData = new FormData();
    formData.append('file', file);
    const response = await fetch('/api/upload',{
        method: 'POST',
        body: formData
    });

    const data: PredictionResult = await response.json();
    return data;
} 