import { View, Text, Button } from 'react-native';
import { router } from 'expo-router';

export default function Login() {
  const handleLogin = () => {
    router.replace('/home');
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Login Page</Text>
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
}
