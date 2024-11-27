import React from "react";
import { createTheme, MantineProvider } from "@mantine/core";
import { IconArrowDownRight, IconArrowUpRight } from "@tabler/icons-react";
import { Center, Group, Paper, RingProgress, SimpleGrid, Text } from "@mantine/core";

import "@mantine/core/styles.css";

const theme = createTheme({
    /** Put your mantine theme override here */
});

export const CardOverCard = () => {
    return (
        <MantineProvider theme={theme}>
            <div>CardOverCard</div>
            <StatsRing />
        </MantineProvider>
    );
};

const icons = {
    up: IconArrowUpRight,
    down: IconArrowDownRight,
};

const data = [
    { label: "Page views", stats: "456,578", progress: 65, color: "teal", icon: "up" },
    { label: "New users", stats: "2,550", progress: 72, color: "blue", icon: "up" },
    {
        label: "Orders",
        stats: "4,735",
        progress: 52,
        color: "red",
        icon: "down",
    },
];

export function StatsRing() {
    const stats = data.map((stat) => {
        const Icon = icons[stat.icon];
        return (
            <Paper withBorder radius="md" p="xs" key={stat.label}>
                <Group>
                    <RingProgress
                        size={80}
                        roundCaps
                        thickness={8}
                        sections={[{ value: stat.progress, color: stat.color }]}
                        label={
                            <Center>
                                <Icon size={20} stroke={1.5} />
                            </Center>
                        }
                    />

                    <div>
                        <Text c="dimmed" size="xs" tt="uppercase" fw={700}>
                            {stat.label}
                        </Text>
                        <Text fw={700} size="xl">
                            {stat.stats}
                        </Text>
                    </div>
                </Group>
            </Paper>
        );
    });

    return <SimpleGrid cols={{ base: 1, sm: 3 }}>{stats}</SimpleGrid>;
}
