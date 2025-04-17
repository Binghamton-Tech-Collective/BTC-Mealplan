import { Link, Stack } from 'expo-router';
import { Text, View, Image } from 'react-native';

export default function LoadingPage() {
  return (
    <View className='flex-1 justify-center items-center bg-white'>

      <View className='w-32 h-32 rounded-full bg-gray-300 mb-4'/>
      <Text className='text-base text-gray-700 mb-8'>Logo</Text>
      <View className='w-10 h-10 rounded-full bg-gray-300 mb-4'/>
      <Text className='text-sm text-gray-500'>Loading icon</Text>
      <View className='p-24'/>
    </View>
  );
}
