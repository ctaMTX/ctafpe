import pygame


def extract_animations(file_path):
    animations = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        start_line = -1

        for i, line in enumerate(lines):
            if line.strip() == ";AIAnims":
                start_line = i + 1
                break

        if start_line != -1:
            anim_lines = lines[start_line:]
            for anim_line in anim_lines:
                anim_parts = anim_line.strip().split('=')
                if len(anim_parts) == 2:
                    anim_name, anim_frames = anim_parts[0].strip(), anim_parts[1].strip()
                    animations.append((anim_name, anim_frames))

    return animations


def view_animations(animations):
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("ctaFPE")

    clock = pygame.time.Clock()
    running = True

    current_animation_index = 0
    current_frame_index = 0
    animation_frames = []

    while running:
        screen.fill((255, 255, 255))

        if animations:
            current_animation = animations[current_animation_index]
            current_animation_name = current_animation[0]
            current_animation_frames = current_animation[1]

            if current_frame_index >= len(animation_frames):
                animation_frames = current_animation_frames.split(',')
                animation_frames = [frame.strip() for frame in animation_frames]

            if current_frame_index < len(animation_frames):
                frame_number = int(animation_frames[current_frame_index])
                frame_text = f"Animation: {current_animation_name} - Frame: {frame_number}"
                frame_surface = pygame.font.SysFont(None, 30).render(frame_text, True, (0, 0, 0))
                screen.blit(frame_surface, (10, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_frame_index += 1
        if current_frame_index >= len(animation_frames):
            current_frame_index = 0
            current_animation_index += 1
            if current_animation_index >= len(animations):
                current_animation_index = 0

        clock.tick(10)  # Adjust the frame rate here

    pygame.quit()

def main():
    fpe_file = "model.fpe"
    animations = extract_animations(fpe_file)

    if animations:
        view_animations(animations)
    else:
        print("No animations found in the FPE file.")

    print("Finished")

if __name__ == '__main__':
    main()
