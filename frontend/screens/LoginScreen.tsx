import { zodResolver } from '@hookform/resolvers/zod';
import { router } from 'expo-router';
import * as SecureStore from 'expo-secure-store';
import { useForm, Controller } from 'react-hook-form';
import { View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import * as z from 'zod';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Text } from '@/components/ui/text';

const loginSchema = z.object({
  email: z
    .string()
    .email('Please enter a valid email address')
    .min(1, 'Please enter an email address'),
  password: z.string().min(1, 'Please enter a password'),
});

type LoginData = z.infer<typeof loginSchema>;

export default function LoginScreen() {
  const { control, handleSubmit } = useForm<LoginData>({
    resolver: zodResolver(loginSchema),
  });

  async function save(key: string, value: string) {
    await SecureStore.setItemAsync(key, value);
  }

  const onLogin = async (data: LoginData) => {
    try {
      await save('email', data.email);
      await save('password', data.password);
      router.replace('/home');
    } catch (error) {
      console.log('Error saving user credentials: ', error);
    }
  };

  return (
    <SafeAreaView className="flex-1 bg-green-500">
      <View className="flex-1 justify-center px-4">
        <View className="gap-y-4">
          <Text>Email Address</Text>
          <Controller
            control={control}
            name="email"
            render={({ field: { onChange, value } }) => (
              <Input
                value={value}
                onChangeText={onChange}
                placeholder="Email"
                autoCapitalize="none"
                autoCorrect={false}
                keyboardType="email-address"
              />
            )}
          />
          <Text>Password</Text>
          <Controller
            control={control}
            name="password"
            render={({ field: { onChange, value } }) => (
              <Input
                secureTextEntry
                placeholder="Enter Password"
                value={value}
                onChangeText={onChange}
              />
            )}
          />
          <Button onPress={handleSubmit(onLogin)}>
            <Text>Login</Text>
          </Button>
        </View>
      </View>
    </SafeAreaView>
  );
}
