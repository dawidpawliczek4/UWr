type User = {
    type: 'user'; // Discriminant property
    name: string;
    age: number;
    occupation: string;
};

type Admin = {
    type: 'admin'; // Discriminant property
    name: string;
    age: number;
    role: string;
};

export type Person = User | Admin;

export const persons: Person[] = [
    {
        type: 'user',
        name: "Jan Kowalski",
        age: 17,
        occupation: "Student",
    },
    {
        type: 'admin',
        name: "Tomasz Malinowski",
        age: 20,
        role: "Administrator",
    },
];

// Type Guards
export function isAdmin(person: Person): person is Admin {
    return person.type === 'admin';
}

export function isUser(person: Person): person is User {
    return person.type === 'user';
}

// Updated logPerson function
export function logPerson(person: Person) {
    let additionalInformation: string = '';

    if (isAdmin(person)) {
        additionalInformation = person.role;
    } else if (isUser(person)) {
        additionalInformation = person.occupation;
    }

    console.log(` - ${person.name}, ${person.age}, ${additionalInformation}`);
}

// Test the function
persons.forEach(logPerson);
