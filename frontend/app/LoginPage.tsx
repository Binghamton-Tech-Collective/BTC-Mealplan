import { Link, Stack } from 'expo-router';
import { Text, View, Image } from 'react-native';

export default function LoginPage() {
  return (
    <View className='flex-1 justify-center items-center bg-white'>


      
      <View className='w-32 h-32 rounded-full bg-gray-300 mb-4'/>
      <Text className='text-base text-black mb-8'>Logo</Text>

      <Text className='text-base text-black mr-80 mb-2'>B-Mail</Text>
      <View className='w-96 h-10 rounded-none bg-gray-300 mb-4'/>
      <Text className='text-base text-black t mr-80 mb-2'>Password</Text>
      <View className='w-96 h-10 rounded-none bg-gray-300 mb-10'/>

      <View className='w-36 h-8 rounded-none bg-gray-300 mb-4'/>

    </View>
  );
}
